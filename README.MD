# clean_html_for_llm

This library provides a method to clean HTML content by removing specified tags and attributes while keeping specified attributes. It is particularly useful for preprocessing HTML data to remove noisy tags, making it easier for language models (LLMs) to understand the HTML and generate accurate responses.
This is super helpful if you are querying LLMs with your HTML data.
![PyPI Version](https://img.shields.io/pypi/v/clean-html-for-llm)
![License](https://img.shields.io/badge/License-MIT-blue.svg)



## Installation

You can install the `clean_html_for_llm` library using pip:

```bash
pip install clean-html-for-llm
```

## Usage

```python
from clean_html_for_llm import clean_html

html_content = '<div id="main" style="color:red">Hello <script>alert("World")</script></div>'
cleaned_html = clean_html(html_content, tags_to_remove=['script'], attributes_to_keep=['id'])
print(cleaned_html)
# Output: '<div id="main">Hello </div>'
```

The `clean_html` function takes the following arguments:

- `html_to_clean` (str): The HTML content to clean.
- `tags_to_remove` (List[str]): List of tags to remove from the HTML content. Default is `['style', 'svg', 'script']`.
- `attributes_to_keep` (List[str]): List of attributes to keep in the HTML tags. Default is `['id', 'href']`.

You can customize the tags and attributes to remove or keep based on your requirements.

## Examples

### Example 1:

```python
html_content = '<div id="content" class="main">This is a <span style="font-size: 18px;">paragraph</span>.</div>'
cleaned_html = clean_html(html_content)
print(cleaned_html)
# Output: '<div id="content">This is a <span>paragraph</span>.</div>'
```

### Example 2:

```python
html_content = '<p class="content">Click <a href="https://example.com">here</a> for more information.</p>'
cleaned_html = clean_html(html_content, tags_to_remove=['a'], attributes_to_keep=['class'])
print(cleaned_html)
# Output: '<p class="content">Click </p>'
```

## License

This library is released under the MIT License. See [LICENSE](LICENSE) for details.
