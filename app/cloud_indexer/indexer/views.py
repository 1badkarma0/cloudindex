from django.shortcuts import render
from django.http import JsonResponse
from .models import IndexedFile, SearchQuery
import subprocess

# View to handle indexing cloud storage
def index_storage(request):
    if request.method == 'POST':
        storage_type = request.POST.get('storage_type')
        storage_path = request.POST.get('storage_path')
        # Use rclone to index the storage
        result = subprocess.run(['rclone', 'ls', f'{storage_type}:{storage_path}'], capture_output=True, text=True)
        if result.returncode == 0:
            # Process the output and save to IndexedFile model
            for line in result.stdout.splitlines():
                parts = line.split(None, 1)
                if len(parts) == 2:
                    file_size, file_path = parts
                    IndexedFile.objects.create(file_name=file_path.split('/')[-1], file_path=file_path, storage_type=storage_type)
            return JsonResponse({'status': 'success', 'message': 'Storage indexed successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': result.stderr})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# View to handle full-text search
def full_text_search(request):
    if request.method == 'GET':
        query_text = request.GET.get('query')
        # Save the search query
        SearchQuery.objects.create(query_text=query_text)
        # Perform the search using Whoosh
        from whoosh.index import open_dir
        from whoosh.qparser import QueryParser
        ix = open_dir("indexdir")
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema).parse(query_text)
            results = searcher.search(query)
            files = [{'file_name': result['file_name'], 'file_path': result['file_path']} for result in results]
        return JsonResponse({'status': 'success', 'files': files})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
