# Project Title

Cloud Storage Indexer

# Project Overview

The Cloud Storage Indexer is designed to provide a unified search functionality across multiple cloud storage services. By leveraging rclone for indexing and Whoosh for full-text search, this tool aims to simplify the process of finding files stored in various cloud services. The main goals are to enable efficient indexing and searching of cloud storage data, ensuring users can quickly locate the files they need.

# Features

- Index multiple cloud storage types (S3, OneDrive, WebDAV, SFTP)
- Perform full-text searches across indexed data
- User-friendly interface for managing storage and search queries
- Secure access to cloud storage services
- Efficient handling of large volumes of data

# Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cloud-storage-indexer.git
   cd cloud-storage-indexer
   ```
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure rclone:
   - Follow the rclone documentation to set up your `rclone.conf` file.
   - Place the `rclone.conf` file in the project's root directory.

# Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```
2. Access the application in your web browser at `http://127.0.0.1:8000`.
3. Use the interface to index cloud storage and perform full-text searches.

# Configuration

- `settings.py`: Contains Django settings, including configurations for rclone and Whoosh.
- `rclone.conf`: Configuration file for rclone, specifying cloud storage credentials and settings.
- `indexdir`: Directory where Whoosh indexes are stored.

# Contributing

We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

# Contact Information

For any questions or inquiries, please contact the project maintainers:
- Email: maintainer@example.com
- GitHub: [yourusername](https://github.com/yourusername)
- Issue Tracker: [GitHub Issues](https://github.com/yourusername/cloud-storage-indexer/issues)