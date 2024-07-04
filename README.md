# generate-api-key

This project provides a GitHub Action to generate a secure API key.

---
## Features
- Generate a secure API key
- Mask the key in the logs
- Set the key as an output

---
## Requirements
- Python 3.11+
- `secrets` library

---
## Usage

```yaml
- name: Generate API Key
  uses: <your_github_handle>/generate-api-key@v1.0
  with:
    KEY_LENGTH: <length_of_the_key>
```

<i>where</i>

`KEY_LENGTH` is the length of the API key to be generated. <b>Optional</b>. Defaults to `32`.

To view the generated key, you can access the output from the previous step or job.

---
## References

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
2. [Python `secrets` Library](https://docs.python.org/3/library/secrets.html)



![Custom Badge](https://rennf93.github.io/project-assets/images/rf-icon.png)