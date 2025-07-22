AI Art Detector for SENG 474 Project

By sofiiak13, kedfree, ssianen, jas-wei

Download our dataset via Google Drive: [https://drive.google.com/drive/folders/1F1LxmTDe8oy9KEKCgCGSUMAZuHX4ebRJ?usp=drive_link ](https://drive.google.com/file/d/1f9Yp0hJyGDFi5U9SNUPQnnOuRdLL_auA/view?usp=sharing)

The dataset was created from a combination of the following Kaggle datasets:
- Ravidu Silva, “AI-ArtBench,” Kaggle.com, 2025. https://www.kaggle.com/datasets/ravidussilva/real-ai-art 
- Alok Pandey, “A Dataset of 11,300 Labeled AI Generated Images,” Kaggle.com, 2025. https://www.kaggle.com/datasets/aloktantrik/a-dataset-of-34500-labeled-images
- Tristan Zhang, “ai-generated-images-vs-real-images,” Kaggle.com, 2025. https://www.kaggle.com/datasets/tristanzhang32/ai-generated-images-vs-real-images.

Update: Two corrupted images in 0-Human were replaced with well-known artworks, Leonardo Da Vinci's 'Mona Lisa' and Johannes Vermeer's 'Girl with a Pearl Earring' https://artistro.com/blogs/news/30-most-famous-artworks-in-history-the-greatest-art-of-all-time

To install the required packages, run: pip install torch torchvision torchaudio numpy scikit-learn seaborn matplotlib 

To create a python virtual environment, cd into the project directory and then run: python3 -m venv myEnvDir

To activate the python virtual environment, run: source myEnvDir/bin/activate
