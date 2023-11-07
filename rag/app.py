# Third party libs
from flask import Flask, jsonify, make_response, request

# Custom libs
import chains


# Initialize the application chain
# chain = chains.assistant_chain("Bob").getChain()
chain = chains.DocumantationChain("https://docs.smith.langchain.com").get_chain()


app = Flask(__name__)


# Handle HTTP POST request
@app.route("/", methods=["POST"])
def chat():
    if not request.is_json:
        return make_response(
            jsonify(
                {
                    "success": False,
                    "error": "Unexpected error, request is not in JSON format",
                }
            ),
            400,
        )

    try:
        data = request.json
        user_input = data["message"]
        result = chain.invoke({"question": user_input})

        return jsonify({"success": True, "data": result})
    except:  # pylint: disable=bare-except
        return make_response(
            jsonify(
                {
                    "success": False,
                    "error": "Unexpected error: failed to send the message",
                }
            ),
            400,
        )
