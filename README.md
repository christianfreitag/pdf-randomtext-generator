# Random PDF Generator

This Python script generates random PDF files using the `reportlab` and `faker` libraries.

![Sample Image](sample_image.png)

## Dependencies

- `reportlab`: For generating PDF files.
- `faker`: For generating random text.

You can install these dependencies using pip:

```bash
pip install reportlab faker
```

## Usage

The script generates PDF files with random text. The number of PDFs to generate and the output directory can be specified.

```python
# Generate 5 PDFs in the "output" directory
generate_pdfs(5, "output")
```

By default, it generates the PDFs in a directory named "generated".

## Functions

- `create_random_pdf(file_name, num_pages=3)`: Creates a random PDF with the specified file name and number of pages. Each page contains random text.

- `generate_pdfs(num_pdfs, output_dir="generated")`: Generates the specified number of PDFs in the specified output directory. Each PDF has a random UUID as its file name.

## Example

To generate a single PDF, you can run:

```python
generate_pdfs(1)
```

This will generate a PDF with random text in the "generated" directory.