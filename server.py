from app.main import api as app

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)