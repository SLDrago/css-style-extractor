# CSS Style Extractor

This Python script extracts all the CSS code from `<style>` tags in an HTML file and writes it into a separate `style.css` file. There are two versions of this script:

1. **Style Remover**: Extracts the CSS and removes the `<style>` tags and their content from the original HTML file.
2. **Style Preserver**: Extracts the CSS but leaves the `<style>` tags and their content intact in the original HTML file.

## Features

- Extracts inline CSS from `<style>` tags in an HTML file.
- Saves the extracted CSS into a `style.css` file.
- Two versions available:
  - **Style Remover**: Removes the extracted styles from the original HTML.
  - **Style Preserver**: Retains the original HTML unchanged.

## Prerequisites

- Python 3.x

## Installation

Clone the repository or download the script directly:

```bash
git clone https://github.com/SLDrago/css-style-extractor.git
cd css-style-extractor
```

## Usage

### Style Remover

This version extracts the CSS from the HTML file and removes the `<style>` tags from the original file.

### Style Preserver

This version extracts the CSS from the HTML file but leaves the `<style>` tags and their content in the original HTML.

### Running the Script

To run either version, replace `'index.html'` with the path to your HTML file and `'style.css'` with the desired output path for the CSS file.
Or you can add this script to your file that contain '.html' file and add the file name to the script from a text editor and run the correct script as follow,

```bash
python3 script_name.py
```

### Example

```python
# Example usage:
extract_and_remove_styles('index.html', 'style.css')
```

or

```python
# Example usage:
extract_and_preserve_styles('index.html', 'style.css')
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute, feel free to fork the repository and submit a pull request.
