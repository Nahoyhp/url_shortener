import my_util


def test_util():
    url = "www.google.com"
    http = "http://" + url
    https = "https://" + url
    assert my_util.removeHttp(url) == url
    assert my_util.removeHttp(http) == url
    assert my_util.removeHttp(https) == url


def test_generate_shorten_url():
    assert my_util.generate_shorten_url(5) != my_util.generate_shorten_url(5)
