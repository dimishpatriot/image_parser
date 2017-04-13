from urllib.parse import quote, urlsplit, urlunsplit


def transform(iri):  # преобразует кириллицу в URI
    parts = urlsplit(iri)
    uri = urlunsplit((parts.scheme, parts.netloc.encode('idna').decode(
        'ascii'), quote(parts.path), quote(parts.query, '='), quote(parts.fragment),))
    return uri
