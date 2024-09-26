# Log Cleanup Automator

This Ansible playbook automates the process of cleaning up old log files in a specified application directory. Originally built for Cortex, it can be adapted for use with other applications. This playbook helps reduce toil associated with manual log management and disk space maintenance.

## Prerequisites

- Ansible 2.9 or higher
- Target Linux server(s) with SSH access
- Sudo privileges on the target server(s)
- A privileged user account on the target server(s)

## Usage

```bash
ansible-playbook ansible-log-cleanup-playbook.yml -i inventory.ini -e "privileged_account=account_name level=1"
```

Ensure your inventory file (`inventory.ini`) contains the target host(s) where you want to perform the log cleanup operation.

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `privileged_account` | The user account under which the cleanup operation should be performed | None (Required) |
| `level` | Determines whether files should be deleted (0 for no deletion, any other value for deletion) | None (Required) |
| `application_base_path` | The base directory path of the application | "/opt/myapp" |
| `application_log_path` | The directory path where log files are stored | "/opt/myapp/logs" |

## Tasks

1. Log start time: Records the start time of the playbook execution in syslog.
2. Check application path: Verifies that the specified application base path exists.
3. Find old log files: Locates log files older than 30 days in the specified log directory.
4. Generate deletion list: Creates a list of log files to be deleted.
5. Display deletion list: Shows the list of files to be deleted (for debugging purposes).
6. Delete log files: Removes the old log files if the 'level' variable is not set to '0'.
7. Log end time: Records the end time of the playbook execution in syslog.

## Expected Outcome

This playbook will safely clean up old log files within the specified application directory:

- It identifies log files older than 30 days.
- It only deletes files if the 'level' variable is not set to '0', providing a safeguard against accidental deletion.
- It logs the start and end times of the operation in syslog for auditing purposes.
- It continues execution even if individual file deletions fail, ensuring robustness.
- It provides debugging information about the files to be deleted before performing the deletion.

By automating this process, it helps maintain optimal disk space usage, reduces the risk of filling up disk space with old logs, and saves time that would otherwise be spent on manual log file management.

## Author

Nanven Faden (nanvenfaden@gmail.com)

## License

This script is proprietary and intended for internal use only. All rights reserved.

## Notes

- The playbook is designed to be flexible and can be adapted for use with applications other than Cortex.
- Always test the playbook in a non-production environment before running it on production systems.
- Ensure that the `privileged_account` has the necessary permissions to access and delete the log files.
- The playbook ignores errors when finding log files to ensure it continues even if there are permission issues in some directories.
- there is an extra script on how to use ansible to install an nginx server.
