import pytest


def test_get_comments_byPostId(
        g_post_posts, g_posts_id_comments, g_faker, l_comments_by_postId):
    """
        GIVEN typicode service is up and running
        WHEN a client calls GET /comments/{postId} to
        retrieve a post comment
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": g_faker.random_int(0, 20),
        "title": g_faker.word()
    }
    post_posts_rsp = g_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))
    payload["body"] = g_faker.text()
    payload["email"] = g_faker.email()

    post_comment_rsp = g_posts_id_comments(
        post_posts_rsp.json()["id"], "POST", payload)

    pytest.assume(
        post_comment_rsp.status_code == 201,
        "returned status code was {}".format(post_comment_rsp.status_code))
    queryParams = {
        "postId": post_comment_rsp.json()["id"]
    }
    get_comments_rsp = l_comments_by_postId(params=queryParams)
    # since the backend doesn't reaaly create comment, verify if response is
    # empty. If the endpoint allowed for actual comments creation
    # then I'd verify if the created comment was equal to actual
    pytest.assume(
        get_comments_rsp.status_code == 200,
        "returned status code was {}".format(get_comments_rsp.status_code))
    pytest.assume(
        len(get_comments_rsp.json()) == 0,
        "returned data array not empty {}".format(
            get_comments_rsp.json()))


@pytest.mark.parametrize("verb", ["DELETE", "PATCH", "PUT"])
def test_get_comments_byPostId_invalidMethod(verb, l_comments_by_postId):
    """
        GIVEN typicode service is up and running
        WHEN a client calls /comments/{postId} with non supported verb
        THEN a 405 status code and correct json response
        should be returned.
    """
    queryParams = {
        "postId": 3
    }
    get_comments_rsp = l_comments_by_postId(verb=verb, params=queryParams)
    pytest.assume(
        get_comments_rsp.status_code == 405,
        "returned status code was {}".format(get_comments_rsp.status_code))
