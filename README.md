## Cyber Security Base MOOC - Course Project I

The purpose of this project is to create a web app with security issues from [OWASP Top Ten](https://owasp.org/www-project-top-ten/) and provide fixes to them.

The project implements a simple banking app with features such as logging in and transferring money to other users.

The app is implemented in Python, using Django's starter template.

### Running the app (Linux)

```python3 manage.py runserver```

### Overview of intentional vulnerabilities

| ID | Description      | OWASP Top Ten category | CWE id | link to code |
| -----------------| ---------------- | ---------------------- | ------ | ------------ |
| 1 | The backend source code and database are publicly available to anyone | A01:2021 Broken Access Control | 552 | N/A |

#### Vulnerability 1 - CWE 552

In this project, all files and directories are publicly available to anyone on the internet because a public GitHub repository is used. Currently, this is the most severe security vulnerability of this project as it provides potential attackers a window to how the application works. This, in turn, allows attackers to plan a range of attacks - for example, a publicly available database schema helps to plan an injection attack. However, since this project has the database pushed to the public repository, the attackers need not bother with planning injections - the (sensitive) data is already on a silver platter, ready to be exploited!

To mitigate this vulnerability, the CWE mentions disabling public access [1]. In practice, GitHub repository settings have a simple toggle between public and private visibility. Additionally, it might be a good idea to include only non-sensitive development data in the repository and have another, more robust and isolated solution to handling production data. [GitHub Docs](https://docs.github.com/en/code-security/getting-started/securing-your-repository) has more on features related to repository security.

### References

[1] https://cwe.mitre.org/data/definitions/552.html


#
More info on Cyber Security Base: https://cybersecuritybase.mooc.fi/
