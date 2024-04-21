# Codey

This is my first attempt at using LLMs to write a coding buddy. This was written
on an Apple Silicon laptop and requires that the model chosen fits within the
memory constraints of your system.

## Getting Started

Choose a model. You'll need to choose one that fits within your available
memory, this defaults to llama3:latest which is one of the smallest models I can
find. Set your model in `my_model` on line 19.

Setup a virtual env

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Start the server

```bash
streamlit run codey.py
```

## Questions

Feel free to ask questions and file issues, but this is really nothing more than some
glue holding together streamlit and llama_index. I'm happy to help but I'm no
expert and you may need to ask around those communities for assistance. 

## Further reading

- [llama-index starter tutorial](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/)
- [Streamlit](https://streamlit.io/)
- [LLM_AppDev-HandsOn by sroecker](https://github.com/sroecker/LLM_AppDev-HandsOn)

## License

This project is under BSD-3-Clause license.

Copyright (c) 2024, Jeff Welling
