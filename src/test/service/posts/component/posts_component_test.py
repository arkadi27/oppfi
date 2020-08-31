import pytest
import requests


def test_posts_retrieve_posts(l_get_posts, l_posts_by_id):
    """
        GIVEN typicode service is up and running
        WHEN a client calls GET /posts
        THEN a 200 status code and correct json response
        should be returned.
    """
    get_posts_rsp = l_get_posts
    pytest.assume(get_posts_rsp.status_code == 200)

    for post in get_posts_rsp.json():
        get_post_byid_rsp = l_posts_by_id(post['id'])
        pytest.assume(
            get_post_byid_rsp.status_code == 200,
            "returned status code was {}".format(
                get_post_byid_rsp.status_code))
        pytest.assume(
            get_post_byid_rsp.json() == post,
            "expected data not equal to actual")


def test_posts_create_post(l_post_posts, l_posts_by_id, faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls POST /posts
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": faker.random_int(0, 20),
        "title": faker.word(),
        "body": faker.text()
    }
    post_posts_rsp = l_post_posts(payload)
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

    # verifying the created data wasn't created in the backend
    # and shoud return a 404
    pytest.assume(
        l_posts_by_id(post_posts_rsp.json()["id"]).status_code == 404)


@pytest.mark.parametrize("verb", ["DELETE", "PATCH", "PUT"])
def test_posts_invalid_method(l_posts_url, verb):
    """
        GIVEN typicode service is up and running
        WHEN a client calls DELETE, PATCH OR PUT /posts
        THEN a 405 status code is returned.
    """
    response = requests.request(verb, l_posts_url)
    # assert returned status code i 405
    pytest.assume(
        response.status_code == 405,
        "returned status code was {}".format(response.status_code))


def test_postId_update_post(l_get_posts, l_post_posts, l_posts_by_id, faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls PUT /posts
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": faker.random_int(0, 20),
        "title": faker.word(),
        "body": faker.text()
    }
    rsp = l_posts_by_id(l_get_posts.json()[0]['id'], "PUT", payload)
    pytest.assume(
        rsp.status_code == 201,
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


def test_postId_delete_post(l_post_posts, l_posts_by_id, faker):
    """
        GIVEN typicode service is up and running
        WHEN a client calls DELETE /posts/id
        THEN a 200 status code and correct json response
        should be returned.
    """
    payload = {
        "userId": faker.random_int(0, 20),
        "title": faker.word(),
        "body": faker.text()
    }
    post_posts_rsp = l_post_posts(payload)
    pytest.assume(
        post_posts_rsp.status_code == 201,
        "returned status code was {}".format(post_posts_rsp.status_code))
    rsp = l_posts_by_id(post_posts_rsp.json()['id'], "DELETE")
    pytest.assume(
        rsp.status_code == 200,
        "returned status code was {}".format(rsp.status_code))


@pytest.mark.me
def test_postId_invalid_method(l_get_posts, l_posts_by_id):
    """
        GIVEN typicode service is up and running
        WHEN a client calls OPTIONS /postId
        THEN a 405 status code is returned.
    """
    response = l_posts_by_id(l_get_posts.json()[0]['id'], "OPTIONS")
    # assert returned status code i 405
    pytest.assume(
        response.status_code == 405,
        "returned status code was {}".format(response.status_code))
