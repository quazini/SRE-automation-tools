
# Secure File Copy Automator

This Ansible playbook automates the process of securely copying files or directories within the same Linux server using regular expressions, reducing toil associated with manual file management tasks while maintaining security best practices.

## Prerequisites

- Ansible 2.9 or higher
- Target Linux server with SSH access
- Sudo privileges on the target server

## Usage

```bash
ansible-playbook copy_files_linux_serevr_regex_playbook.yml -i inventory.ini -e "source_path=/path/to/source file_or_directory=file_pattern destination_path=/path/to/destination user_account=username"
```

Ensure your inventory file (`inventory.ini`) contains the target host(s) where you want to perform the secure file copy operation.

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `source_path` | The directory path where the file(s) or directory to be copied is located | None (Required) |
| `file_or_directory` | The name or pattern of the file(s) or directory to be copied | None (Required) |
| `destination_path` | The directory path where the file(s) or directory should be copied to | None (Required) |
| `user_account` | The user account under which the copy operation should be performed | None (Required) |

## Tasks

1. Log start time: Records the start time of the playbook execution in syslog.
2. Validate user inputs: Checks if the provided paths and user account are valid and authorized.
3. Verify source existence: Ensures the source file(s) or directory exists using the specified pattern.
4. Check destination: Verifies the destination path and creates it if it doesn't exist.
5. Backup existing files: Creates backups of any existing files at the destination that match the pattern.
6. Copy files: Performs the actual file or directory copy operation for all matching files.
7. Log end time: Records the end time of the playbook execution in syslog.

## Expected Outcome

This playbook will safely copy files or directories within the same Linux server using regular expressions, adhering to strict security practices:

- It only allows operations within approved directories, preventing access to sensitive system locations.
- It uses regex patterns to find and copy multiple files matching a given pattern.
- It creates backups of existing files at the destination before copying.
- It preserves file permissions and ownership during the copy operation.
- It logs the start and end times of the operation in syslog for auditing purposes.
- It performs various security checks, such as verifying user IDs and approved directories.

By automating this process, it reduces the risk of human error in file management tasks, enhances security, and saves time that would otherwise be spent on manual file operations.

## Author

Nanven Faden (nanvenfaden@gmail.com)

## License

This script is proprietary and intended for internal use only. All rights reserved.
