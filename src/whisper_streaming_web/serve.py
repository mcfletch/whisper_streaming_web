"""Stand-alone script for running the whisper fastapi websocket server"""

import uvicorn, logging, argparse
from .clargs import get_options


def main():
    args = get_options().parse_args()
    uvicorn.run(
        'whisper_streaming_web.whisper_fastapi_online_server:app',
        host=args.host,
        port=args.port,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()
