from mysite.settings import SPECTACULAR_SETTINGS


def preprocess_exclude_path(endpoints, **kwargs):
    """
        preprocessing hook that filters out listed in EXCLUDE_PATH
    """
    return [
        (path, path_regex, method, callback)
        for path, path_regex, method, callback in endpoints
        if not (path in SPECTACULAR_SETTINGS['EXCLUDE_PATH'])
    ]
