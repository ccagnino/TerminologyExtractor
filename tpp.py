# Text Pre-Processing: Lowercasing, tokenization, POS tagging, phrase chunking, lemmatization.

import fitz, nltk, re, string

def pdf_to_text(document):
    '''Takes in a .pdf document, returns it as plain text.
    '''
    doc = fitz.open(document)  # Open a .pdf file with PyMuPDF
    text = ''
    # Loop over every page in .pdf file, get text and append it to the empty string
    for page in doc:
        text += page.get_text()
    return text

def clean_text(document):
    '''Returns lowercased text.
    '''
    lowercase_doc = document.lower()
#   document = document.translate(str.maketrans('', '', string.punctuation))
    no_punct_doc = re.sub(r'[^\w\s\]|[\n\r]', ' ', lowercase_doc)
    no_punct_doc = re.sub(r'\s+', ' ', no_punct_doc)
#   processed_doc = document.replace('\n',' ')
#def clean_text(text):
#    text = text.lower()
#    text = re.sub('\[.*?\]', '', text)
#    text = re.sub('<.*?>+', '', text)
#    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#    text = re.sub('\n', '', text)
#    text = re.sub('\w*\d\w*', '', text)
#    return text
    return no_punct_doc

def pos_tagging(document):
    '''Removes punctuation and returns tagged tokens.
    '''
    tokens = nltk.word_tokenize(text)  # Tokenize text
    sentences = nltk.sent_tokenize(text)
    filtered = [token for token in tokens if token.isalpha()] # Filters out everything that is not alphabetic
    tagged = nltk.pos_tag(filtered)  # POS tagging tokens

#    for sentence in sentences:
#        sentence_tokens = nltk.word_tokenize(sentence)
        # Find the tagged tokens that belong to the sentence
#        sentence_tagged_tokens = [tagged for tagged in tagged if tagged[0] in sentence_tokens]
#    return sentence_tagged_tokens
#    return tagged
#    print(sentences)

file = 'sample.pdf'
print(clean_text(pdf_to_text(file)))
#pos_tagging()

def chunking(document):
    '''
    '''

   # defines grammar for chunking noun phrases
    chunk_grammar_rules = r'''
        NP: {<DT\$>?<JJ>*<NN.*>+} # noun phrase
            {<DT\$>?<JJ>*<NN.*>*<of><JJ>*<NN.*>*}
	    '''
    chunk_parser = nltk.RegexpParser(chunk_grammar_rules)
    chunked = chunk_parser.parse(tagged)  # chunk tagged tokens
    #print(chunked)

def get_chunks(chunked, chunk_type='NP'):
    
    all_chunks = []
    # chunked sentences are in the form of nested trees
    for tree in chunked:
        chunks = []
        # iterate through subtrees / leaves to get individual chunks
        raw_chunks = [subtree.leaves() for subtree in tree.subtrees()
                      if subtree.node == chunk_type]
        for raw_chunk in raw_chunks:
            chunk = []
            for word_tag in raw_chunk:
            	# drop POS tags, keep words
                chunk.append(word_tag[0])
            chunks.append(' '.join(chunk))
        all_chunks.append(chunks)
    
    return all_chunks
#print(get_chunks(chunked))
