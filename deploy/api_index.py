"""Vercel entry point for the hosted License Navigator. Copied to api/index.py by deploy/stage.py: edit this file.

The FastAPI preset (deploy/vercel.json) routes every path here and serves no files; deploy/smoke.py checks that no
source or data file is reachable.
"""

from counselmode_licenses.http import create_app

app = create_app()
