from citation.csl_constants import (
    ARTICLE,
    ARTICLE_JOURNAL,
    ARTICLE_MAGAZINE,
    ARTICLE_NEWSPAPER,
    BROADCAST,
    CHAPTER,
    ENTRY_DICTIONARY,
    ENTRY_ENCYCLOPEDIA,
    GRAPHIC,
    LEGAL_CASE,
    LEGISLATION,
    MOTION_PICTURE,
    PAPER_CONFERENCE,
    PERSONAL_COMMUNICATION,
    POST,
    POST_WEBLOG,
    SONG,
    SPEECH,
)

ARTWORK = "ARTWORK"
AUDIO_RECORDING = "AUDIO_RECORDING"
BILL = "BILL"
BLOG_POST = "BLOG_POST"
BOOK = "BOOK"
BOOK_SECTION = "BOOK_SECTION"
CASE = "CASE"
CONFERENCE_PAPER = "CONFERENCE_PAPER"
DICTIONARY_ENTRY = "DICTIONARY_ENTRY"
DOCUMENT = "DOCUMENT"
EMAIL = "EMAIL"
ENCYCLOPEDIA_ARTICLE = "ENCYCLOPEDIA_ARTICLE"
FILM = "FILM"
FORUM_POST = "FORUM_POST"
HEARING = "HEARING"
INSTANT_MESSAGE = "INSTANT_MESSAGE"
INTERVIEW = "INTERVIEW"
JOURNAL_ARTICLE = "JOURNAL_ARTICLE"
LETTER = "LETTER"
MAGAZINE_ARTICLE = "MAGAZINE_ARTICLE"
MANUSCRIPT = "MANUSCRIPT"
MAP = "MAP"
NEWSPAPER_ARTICLE = "NEWSPAPER_ARTICLE"
PATENT = "PATENT"
PODCAST = "PODCAST"
PREPRINT = "PREPRINT"
PRESENTATION = "PRESENTATION"
RADIO_BROADCAST = "RADIO_BROADCAST"
REPORT = "REPORT"
SOFTWARE = "SOFTWARE"
STATUTE = "STATUTE"
THESIS = "THESIS"
TV_BROADCAST = "TV_BROADCAST"
VIDEO_RECORDING = "VIDEO_RECORDING"
WEBPAGE = "WEBPAGE"

ZOTERO_TO_CSL_MAPPING = {
    ARTWORK: GRAPHIC.lower(),
    AUDIO_RECORDING: SONG.lower(),
    BILL: BILL.lower(),
    BLOG_POST: POST_WEBLOG.lower(),
    BOOK: BOOK.lower(),
    BOOK_SECTION: CHAPTER.lower(),
    CASE: LEGAL_CASE.lower(),
    CONFERENCE_PAPER: PAPER_CONFERENCE.lower(),
    DICTIONARY_ENTRY: ENTRY_DICTIONARY.lower(),
    DOCUMENT: DOCUMENT.lower(),
    EMAIL: PERSONAL_COMMUNICATION.lower(),
    ENCYCLOPEDIA_ARTICLE: ENTRY_ENCYCLOPEDIA.lower(),
    FILM: MOTION_PICTURE.lower(),
    FORUM_POST: POST.lower(),
    HEARING: HEARING.lower(),
    INSTANT_MESSAGE: PERSONAL_COMMUNICATION.lower(),
    INTERVIEW: INTERVIEW.lower(),
    JOURNAL_ARTICLE: ARTICLE_JOURNAL.lower(),
    LETTER: PERSONAL_COMMUNICATION.lower(),
    MAGAZINE_ARTICLE: ARTICLE_MAGAZINE.lower(),
    MANUSCRIPT: MANUSCRIPT.lower(),
    MAP: MAP.lower(),
    NEWSPAPER_ARTICLE: ARTICLE_NEWSPAPER.lower(),
    PATENT: PATENT.lower(),
    PODCAST: BROADCAST.lower(),
    PREPRINT: ARTICLE.lower(),
    PRESENTATION: SPEECH.lower(),
    RADIO_BROADCAST: BROADCAST.lower(),
    REPORT: REPORT.lower(),
    SOFTWARE: SOFTWARE.lower(),
    STATUTE: LEGISLATION.lower(),
    THESIS: THESIS.lower(),
    TV_BROADCAST: BROADCAST.lower(),
    VIDEO_RECORDING: MOTION_PICTURE.lower(),
    WEBPAGE: WEBPAGE.lower(),
}

CSL_TO_ZOTERO_MAPPING = {value: key for key, value in ZOTERO_TO_CSL_MAPPING.items()}

# BibTeX Entry Types: https://www.bibtex.com/e/entry-types/
BIBTEX_TO_CITATION_TYPES = {
    "article": JOURNAL_ARTICLE,
    "book": BOOK,
    "booklet": BOOK,
    "conference": CONFERENCE_PAPER,
    "inbook": BOOK_SECTION,
    "incollection": BOOK_SECTION,
    "inproceedings": CONFERENCE_PAPER,
    "manual": DOCUMENT,
    "masterthesis": THESIS,
    "misc": DOCUMENT,
    "phdthesis": THESIS,
    "proceedings": CONFERENCE_PAPER,
    "techreport": REPORT,
    "unpublished": DOCUMENT,
}
BIBTEX_TYPE_TO_CSL_MAPPING = {
    "article": ARTICLE_JOURNAL.lower(),
    "book": BOOK.lower(),
    "booklet": BOOK.lower(),
    "conference": PAPER_CONFERENCE.lower(),
    "inbook": CHAPTER.lower(),
    "incollection": CHAPTER.lower(),
    "inproceedings": PAPER_CONFERENCE.lower(),
    "manual": REPORT.lower(),
    "mastersthesis": THESIS.lower(),
    "misc": DOCUMENT.lower(),
    "phdthesis": THESIS.lower(),
    "proceedings": PAPER_CONFERENCE.lower(),
    "techreport": REPORT.lower(),
    "unpublished": ARTICLE.lower(),
    "online": WEBPAGE.lower(),
}

CITATION_TYPE_CHOICES = (
    (ARTWORK, ARTWORK),
    (AUDIO_RECORDING, AUDIO_RECORDING),
    (BILL, BILL),
    (BLOG_POST, BLOG_POST),
    (BOOK, BOOK),
    (BOOK_SECTION, BOOK_SECTION),
    (CASE, CASE),
    (CONFERENCE_PAPER, CONFERENCE_PAPER),
    (DICTIONARY_ENTRY, DICTIONARY_ENTRY),
    (DOCUMENT, DOCUMENT),
    (EMAIL, EMAIL),
    (ENCYCLOPEDIA_ARTICLE, ENCYCLOPEDIA_ARTICLE),
    (FILM, FILM),
    (FORUM_POST, FORUM_POST),
    (HEARING, HEARING),
    (INSTANT_MESSAGE, INSTANT_MESSAGE),
    (INTERVIEW, INTERVIEW),
    (JOURNAL_ARTICLE, JOURNAL_ARTICLE),
    (LETTER, LETTER),
    (MAGAZINE_ARTICLE, MAGAZINE_ARTICLE),
    (MANUSCRIPT, MANUSCRIPT),
    (MAP, MAP),
    (NEWSPAPER_ARTICLE, NEWSPAPER_ARTICLE),
    (PATENT, PATENT),
    (PODCAST, PODCAST),
    (PREPRINT, PREPRINT),
    (PRESENTATION, PRESENTATION),
    (RADIO_BROADCAST, RADIO_BROADCAST),
    (REPORT, REPORT),
    (SOFTWARE, SOFTWARE),
    (STATUTE, STATUTE),
    (THESIS, THESIS),
    (TV_BROADCAST, TV_BROADCAST),
    (VIDEO_RECORDING, VIDEO_RECORDING),
    (WEBPAGE, WEBPAGE),
)


# These need to be CSL compliant
# https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types
CITATION_TYPE_FIELDS = {
    JOURNAL_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "issue",
        "page",
        "collection-title",
        "journalAbbreviation",
        "language",
        "DOI",
        "ISSN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
        "custom",
    ],
    ARTWORK: [
        "title",
        "abstract",
        "medium",
        "dimensions",
        "language",
        "title-short",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "URL",
        "issued",
        "note",
    ],
    AUDIO_RECORDING: [
        "title",
        "abstract",
        "medium",
        "collection-title",
        "volume",
        "number-of-volumes",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "ISBN",
        "title-short",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "URL",
        "issued",
        "note",
    ],
    BILL: [
        "title",
        "abstract",
        "number",
        "container-title",
        "volume",
        "section",
        "page",
        "authority",
        "chapter-number",
        "references",
        "language",
        "URL",
        "title-short",
        "issued",
        "note",
    ],
    BLOG_POST: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "URL",
        "language",
        "title-short",
        "issued",
        "note",
    ],
    BOOK: [
        "title",
        "abstract",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "number-of-pages",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    BOOK_SECTION: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    CASE: [
        "title",
        "abstract",
        "authority",
        "number",
        "container-title",
        "volume",
        "page",
        "references",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    SOFTWARE: [
        "title",
        "abstract",
        "collection-title",
        "version",
        "medium",
        "publisher-place",
        "publisher",
        "genre",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    CONFERENCE_PAPER: [
        "title",
        "abstract",
        "container-title",
        "event-title",
        "publisher-place",
        "publisher",
        "volume",
        "page",
        "collection-title",
        "language",
        "DOI",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    DICTIONARY_ENTRY: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    DOCUMENT: [
        "title",
        "abstract",
        "publisher",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    EMAIL: [
        "title",
        "abstract",
        "title-short",
        "URL",
        "language",
        "license",
        "issued",
        "note",
    ],
    ENCYCLOPEDIA_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "ISBN",
        "title-short",
        "URL",
        "language",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    FILM: [
        "title",
        "abstract",
        "publisher",
        "genre",
        "medium",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    FORUM_POST: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    HEARING: [
        "title",
        "abstract",
        "section",
        "publisher-place",
        "publisher",
        "number-of-volumes",
        "number",
        "page",
        "authority",
        "chapter-number",
        "references",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    INSTANT_MESSAGE: [
        "title",
        "abstract",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    INTERVIEW: [
        "title",
        "abstract",
        "medium",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    LETTER: [
        "title",
        "abstract",
        "genre",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    MAGAZINE_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "issue",
        "page",
        "language",
        "ISSN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    MANUSCRIPT: [
        "title",
        "abstract",
        "genre",
        "publisher-place",
        "number-of-pages",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    MAP: [
        "title",
        "abstract",
        "genre",
        "scale",
        "collection-title",
        "edition",
        "publisher-place",
        "publisher",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    NEWSPAPER_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "publisher-place",
        "edition",
        "section",
        "page",
        "language",
        "title-short",
        "ISSN",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    PATENT: [
        "title",
        "abstract",
        "publisher-place",
        "authority",
        "number",
        "page",
        "call-number",
        "issue",
        "references",
        "status",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    PODCAST: [
        "title",
        "abstract",
        "collection-title",
        "number",
        "medium",
        "dimensions",
        "URL",
        "language",
        "title-short",
        "issued",
        "note",
    ],
    PREPRINT: [
        "title",
        "abstract",
        "genre",
        "publisher",
        "number",
        "publisher-place",
        "collection-title",
        "collection-number",
        "DOI",
        "URL",
        "archive",
        "archive_location",
        "title-short",
        "language",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    PRESENTATION: [
        "title",
        "abstract",
        "genre",
        "publisher-place",
        "event-title",
        "URL",
        "language",
        "title-short",
        "issued",
        "note",
    ],
    RADIO_BROADCAST: [
        "title",
        "abstract",
        "container-title",
        "number",
        "medium",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    REPORT: [
        "title",
        "abstract",
        "number",
        "genre",
        "collection-title",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    STATUTE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "number",
        "page",
        "section",
        "chapter-number",
        "references",
        "language",
        "title-short",
        "URL",
        "issued",
        "note",
    ],
    THESIS: [
        "title",
        "abstract",
        "genre",
        "publisher",
        "publisher-place",
        "number-of-pages",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    TV_BROADCAST: [
        "title",
        "abstract",
        "container-title",
        "number",
        "medium",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    VIDEO_RECORDING: [
        "title",
        "abstract",
        "medium",
        "collection-title",
        "volume",
        "number-of-volumes",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "issued",
        "note",
    ],
    WEBPAGE: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "title-short",
        "URL",
        "language",
        "issued",
        "note",
    ],
}
