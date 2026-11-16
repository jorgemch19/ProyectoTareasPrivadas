"""Application entry point: creates the FastAPI app."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Build the FastAPI application.

    Routes are added in later milestones. The interactive API documentation
    lives under /api/docs, next to the API itself.
    """
    return FastAPI(
        title="Private Tasks",
        docs_url="/api/docs",
        redoc_url=None,
        openapi_url="/api/openapi.json",
    )


app = create_app()
