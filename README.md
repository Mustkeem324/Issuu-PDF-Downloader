# Issuu PDF Downloader

This script is designed to download PDF documents from Issuu using its API. It allows users to input an Issuu document link and automatically fetches the document pages' images, which are then compiled into a PDF file.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `PIL`, `concurrent`, `uuid`

## How to Use

1. Clone or download the repository to your local machine.
2. Install the required Python packages if you haven't already:

    ```
    pip install requests Pillow
    ```
   
3. Run the script by executing `python issuu_pdf_downloader.py`.
4. Input the Issuu document link when prompted.
5. Wait for the script to download and compile the PDF.
6. Find the downloaded PDF in the `output_folder` directory.

## Important Notes

- Make sure to have a stable internet connection as the script relies on fetching images from the Issuu API.
- The script may take some time depending on the document size and your internet speed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
