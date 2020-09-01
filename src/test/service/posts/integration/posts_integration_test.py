import pytest


def test_posts_createComment(g_post_posts, g_posts_id_comments, faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls POST /posts/postId/comments to
        create a post comment
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": faker.random_int(0, 20),
        "title": faker.word()
    }
    post_posts_rsp = g_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))
    payload["body"] = faker.text()
    payload["email"] = faker.email()

    post_comment_rsp = g_posts_id_comments(
        post_posts_rsp.json()["id"], "POST", payload)

    pytest.assume(
        post_comment_rsp.status_code == 201,
        "returned status code was {}".format(post_comment_rsp.status_code))
    # assert returned comment equal to posted comment
    pytest.assume(
        post_comment_rsp.json()["body"] == payload["body"],
        "posted comment was {}, actual comment is {}".format(
            payload["body"], post_comment_rsp.json()["body"]))
    pytest.assume(
        post_comment_rsp.json()["email"] == payload["email"],
        "posted email was {}, actual email is {}".format(
            payload["email"], post_comment_rsp.json()["email"]))

    # for a new post, comment isn't posted in backend
    # verify newly created post comment is empty
    post_comment = g_posts_id_comments(post_comment_rsp.json()['id'])
    pytest.assume(
        len(post_comment.json()) == 0,
        "comment was created in the backend {}".format(post_comment.json()))


def test_posts_comment_invalidMethod(
        g_post_posts, g_posts_id_comments, faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls OPTIONS /posts/postId/comments to
        create a post comment
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": faker.random_int(0, 20),
        "title": faker.word()
    }
    post_posts_rsp = g_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))
    payload["body"] = faker.text()
    payload["email"] = faker.email()

    post_comment_rsp = g_posts_id_comments(
        post_posts_rsp.json()["id"], "OPTIONS", payload)
    pytest.assume(
        post_comment_rsp.status_code == 405,
        "returned status code was {}".format(post_comment_rsp.status_code))
