import streamlit as st
import spacy_streamlit
from spacy_streamlit import visualize_ner
import spacy
import pandas as pd
import docx
import re
from spacy import displacy

nlp = spacy.load('models/nlp_ner1/')


def read_docx(filename):
    doc = docx.Document(filename)
    
    paragraphs = []

    #append each sentence to a list if the sentence isn't empty
    for para in doc.paragraphs[8:]:
        if para.text != '' and para.text != ' ':
            paragraphs.append(re.sub('\xa0', ': ', para.text))
    
    return paragraphs


file = st.file_uploader('Upload a press conference transcript file')


if file:
    paragraphs = read_docx(file)
    # para_yes = [para for para in paragraphs if len(nlp(para).ents)>0]

    # for para in para_yes:
    #     visualize_ner(nlp(para))



    for para in paragraphs:
        doc = nlp(para)
        if len(doc.ents) > 0:
            visualize_ner(doc, labels=nlp.get_pipe("ner").labels)