How to create Virtual Environment
# Creating a Virtual Environment in Python

To create and manage virtual environments:

1. **Install virtualenv**
    ```bash
    pip install virtualenv
    ```

2. **Create a new environment**
    ```bash
    python -m venv myenv
    ```

3. **Activate the environment**
    - Windows:
      ```bash
      myenv\Scripts\Activate
      ```
    - Unix/MacOS:
      ```bash
      source myenv/bin/activate
      ```

4. **Deactivate when done**
    ```bash
    deactivate
    ```

## Key Benefits
- Isolated dependencies
- Project-specific packages
- Prevents conflicts
- Easy environment sharing

## Working with Packages

1. **Install pandas**
    ```bash
    pip install pandas
    ```

2. **Check package version**
    ```bash
    pip show pandas
    # or
    python -c "import pandas; print(pandas.__version__)"
    # or
    pip list | grep pandas
    ```

3. **Install specific version**
    ```bash
    pip install pandas==1.5.3
    ```