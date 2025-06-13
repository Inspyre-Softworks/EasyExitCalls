# Example Usages Directory

This directory contains examples of how to use the `easy_exit_calls` library in various scenarios.

## Installation

### Standard Installation

Before running any of the examples, you must first install the `easy_exit_calls` library. You can do this by running the following command:

```bash
pip install easy-exit-calls
```

### Development Installation

  - Clone the repository and navigate to the root directory:
    ```bash
    git clone https://github.com/Inspyre-Softworks/easy-exit-calls.git
    ```
    Or, if you have github CLI installed:
    ```bash
    gh repo clone Inspyre-Softworks/easy-exit-calls
    ```
    Then navigate to the root directory:
    ```bash
    cd easy-exit-calls
    ```
  - Install with poetry:
    ```bash
    poetry install
    ```

### Running the Examples

After installation, run an example script from the project root:

```bash
python examples/manual_registration.py
```

You can also enable logging output:

```bash
python examples/manual_registration_with_logging.py --log-level DEBUG
```
