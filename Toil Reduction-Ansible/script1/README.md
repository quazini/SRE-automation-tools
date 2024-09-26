# File Copy Automator

This Ansible playbook automates the process of copying files or directories within the same Linux server, reducing toil associated with manual file management tasks. Kindly nte that you cannot use regular expressions to copy files, if you need to take a look at script 2.

## Prerequisites

- Ansible 2.9 or higher
- Target Linux server with SSH access
- Sudo privileges on the target server

## Usage

```bash
ansible-playbook copy_file_linux_server._playbook.yml -i inventory.ini -e "source_path=/path/to/source file_or_directory=file_name destination_path=/path/to/destination user_account=username"
```

Ensure your inventory file (`inventory.ini`) contains the target host(s) where you want to perform the file copy operation.

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `source_path` | The directory path where the file or directory to be copied is located | None (Required) |
| `file_or_directory` | The name of the file or directory to be copied | None (Required) |
| `destination_path` | The directory path where the file or directory should be copied to | None (Required) |
| `user_account` | The user account under which the copy operation should be performed | None (Required) |

## Tasks

1. Log start time: Records the start time of the playbook execution.
2. Validate user inputs: Checks if the provided paths and user account are valid and authorized.
3. Verify source existence: Ensures the source file or directory exists.
4. Check destination: Verifies the destination path and creates it if it doesn't exist.
5. Backup existing files: Creates a backup of any existing files at the destination.
6. Copy files: Performs the actual file or directory copy operation.
7. Log end time: Records the end time of the playbook execution.

## Expected Outcome

This playbook will safely copy files or directories within the same Linux server, adhering to security best practices:

- It only allows operations within approved directories.
- It prevents access to restricted system directories.
- It creates backups of existing files at the destination.
- It preserves file permissions and ownership during the copy operation.
- It logs the start and end times of the operation for auditing purposes.

By automating this process, it reduces the risk of human error in file management tasks and saves time that would otherwise be spent on manual file operations.

## Author

Nanven Faden (nanvenfaden@gmail.com)

## License

This script is proprietary and intended for internal use only. All rights reserved.
