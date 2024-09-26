# Ansible Automation Scripts Collection

This directory contains a collection of Ansible playbooks designed to automate various system administration tasks, reducing toil and improving efficiency in managing Linux servers.

## Overview

These playbooks are designed to handle common tasks that system administrators often face, such as file management and log cleanup. By automating these processes, we can reduce human error, save time, and ensure consistency across our systems.

## Playbooks

1. **File Copy Automator** (`copy_file_linux_server._playbook.yml`)
   - Automates the process of copying files or directories within the same Linux server.
   - Implements security checks and best practices for file operations.

2. **Secure File Copy Automator** (`copy_files_linux_serevr_regex_playbook.yml`)
   - Provides a more secure version of file copy automation, with additional checks and regex pattern matching.
   - Allows for copying multiple files based on patterns.

3. **Log Cleanup Automator** (`ansible-log-cleanup-playbook.yml`)
   - Automates the process of cleaning up old log files in specified application directories.
   - Helps maintain optimal disk space usage and prevents issues related to full disks.

## Prerequisites

- Ansible 2.9 or higher
- Target Linux server(s) with SSH access
- Sudo privileges on the target server(s)
- Appropriate user accounts with necessary permissions on target servers

## General Usage

Each playbook has its own specific usage instructions and required parameters. Please refer to the individual README files for each playbook for detailed usage information.

Generally, playbooks are run using the following command structure:

```bash
ansible-playbook <playbook_name>.yml -i inventory.ini -e "var1=value1 var2=value2"
```

Replace `<playbook_name>` with the name of the playbook you want to run, and provide the necessary variables as extra vars (`-e`).

## Security Considerations

- These playbooks often deal with file operations and system modifications. Always review the playbooks and test them in a non-production environment before running them on production systems.
- Ensure that the user accounts specified in the playbooks have the minimum necessary permissions to perform their tasks.
- Regularly review and update the list of approved and restricted directories in the file copy playbooks to align with your organization's security policies.

## Customization

These playbooks can be customized to fit your specific needs:

- Modify the list of approved and restricted directories in the file copy playbooks.
- Adjust the age threshold for log file deletion in the log cleanup playbook.
- Add additional tasks or checks as needed for your environment.

## Contributing

If you make improvements to these playbooks or create new ones that could be useful to others in the organization, please follow these steps:

1. Create a new branch for your changes.
2. Make your modifications and test thoroughly.
3. Update the relevant README files with any new information.
4. Submit a pull request for review.

## Author

Nanven Faden (nanvenfaden@gmail.com)

## License

These scripts are proprietary and intended for internal use only. All rights reserved.

## Support

For questions, issues, or suggestions regarding these playbooks, please contact the author or open an issue in the internal issue tracking system.
