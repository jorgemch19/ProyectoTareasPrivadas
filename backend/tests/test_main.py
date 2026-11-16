from app.main import create_app


def test_app_publishes_api_docs_under_api_prefix() -> None:
    app = create_app()

    assert app.title == "Private Tasks"
    assert app.docs_url == "/api/docs"
    assert app.openapi_url == "/api/openapi.json"
    assert app.redoc_url is None
