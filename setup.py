from setuptools import setup, find_packages

setup(
    name='clean_html_for_llm',
    version='1.3.0',
    description='A library for cleaning HTML content by removing specified tags and attributes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shubhamofbce/clean-html-for-llm.git',
    author='Shubham Raj',
    author_email='sraj13169@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='html cleaning, html cleaning for llm, html denoise for llm, html denoising for llm, html cleaning for language model, html denoise for language model, html denoising for language model, html cleaning for nlp, html denoise for nlp, html denoising for nlp',
    python_requires='>=3.7',
)
