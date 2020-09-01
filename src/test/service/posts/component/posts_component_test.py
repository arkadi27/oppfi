import pytest
import requests


def test_posts_retrievePosts(g_get_posts, g_posts_by_id):
    """
        GIVEN typicode service is up and running
        WHEN a client calls GET /posts
        THEN a 200 status code and correct json response
        should be returned.
    """
    get_posts_rsp = g_get_posts
    pytest.assume(get_posts_rsp.status_code == 200)

    for post in get_posts_rsp.json():
        get_post_byid_rsp = g_posts_by_id(post['id'])
        pytest.assume(
            get_post_byid_rsp.status_code == 200,
            "returned status code was {}".format(
                get_post_byid_rsp.status_code))
        pytest.assume(
            get_post_byid_rsp.json() == post,
            "expected data not equal to actual")


def test_posts_createPost(g_post_posts, g_posts_by_id, g_faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls POST /posts
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": g_faker.random_int(0, 20),
        "title": g_faker.word(),
        "body": g_faker.text()
    }
    post_posts_rsp = g_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))

    pytest.assume(
            post_posts_rsp.json()["title"] == payload["title"],
            "expected title was {}, actual is {}".format(
                post_posts_rsp.json()["title"],
                payload["title"]))
    pytest.assume(
            post_posts_rsp.json()["body"] == payload["body"],
            "expected body was {}, actual is {}".format(
                post_posts_rsp.json()["body"],
                payload["body"]))
    pytest.assume(
            post_posts_rsp.json()["userId"] == payload["userId"],
            "expected userId was {}, actual is {}".format(
                post_posts_rsp.json()["userId"],
                payload["userId"]))

    # verify the created data wasn't created in the backend
    # and shoud return a 404
    pytest.assume(
        g_posts_by_id(post_posts_rsp.json()["id"]).status_code == 404)


@pytest.mark.parametrize("verb", ["DELETE", "PATCH", "PUT"])
def test_posts_invalidMethod(g_posts_url, verb):
    """
        GIVEN typicode service is up and running
        WHEN a client calls DELETE, PATCH OR PUT /posts
        THEN a 405 status code is returned.
    """
    response = requests.request(verb, g_posts_url)
    # assert returned status code is 405
    pytest.assume(
        response.status_code == 405,
        "returned status code was {}".format(response.status_code))
    # verify response is empty
    pytest.assume(not response.json(), "response wasn't empty")


def test_postId_updatePost(g_get_posts, g_post_posts, g_posts_by_id, g_faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls PUT /posts
        THEN a 201 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": g_faker.random_int(0, 20),
        "title": g_faker.word(),
        "body": g_faker.text()
    }
    rsp = g_posts_by_id(g_get_posts.json()[0]['id'], "PUT", payload)
    pytest.assume(
        rsp.status_code == 200,
        "returned status code was {}".format(rsp.status_code))

    pytest.assume(
            rsp.json()["title"] == payload["title"],
            "expected title was {}, actual is {}".format(
                rsp.json()["title"],
                payload["title"]))
    pytest.assume(
            rsp.json()["userId"] == payload["userId"],
            "expected user id was {}, actual is {}".format(
                rsp.json()["userId"],
                payload["userId"]))
    pytest.assume(
            rsp.json()["body"] == payload["body"],
            "expected body was {}, actual is {}".format(
                rsp.json()["body"],
                payload["body"]))


def test_postId_deletePost(g_post_posts, g_posts_by_id, g_faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls DELETE /posts/id
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": g_faker.random_int(0, 20),
        "title": g_faker.word(),
        "body": g_faker.text()
    }
    post_posts_rsp = g_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))
    rsp = g_posts_by_id(post_posts_rsp.json()['id'], "DELETE")
    pytest.assume(
        rsp.status_code == 200,
        "returned status code was {}".format(rsp.status_code))


def test_postId_invalidMethod(g_get_posts, g_posts_by_id):
    """
        GIVEN typicode service is up and running
        WHEN a client calls OPTIONS /postId
        THEN a 405 status code is returned.
    """
    response = g_posts_by_id(g_get_posts.json()[0]['id'], "OPTIONS")
    # assert returned status code i 405
    pytest.assume(
        response.status_code == 405,
        "returned status code was {}".format(response.status_code))
    # verify response is empty
    pytest.assume(not response.json(), "response wasn't empty")
