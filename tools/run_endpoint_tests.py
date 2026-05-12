import urllib.request
import json
import sys

def do_get(path):
    url = base + path
    req = urllib.request.Request(url, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read().decode('utf-8', errors='replace')
            print(f"GET {path} -> {r.status} {r.reason}")
            print(data[:2000])
    except Exception as e:
        print(f"GET {path} failed: {e}")


def do_post(path, payload):
    url = base + path
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = r.read().decode('utf-8', errors='replace')
            print(f"POST {path} -> {r.status} {r.reason}")
            print(resp[:4000])
    except Exception as e:
        print(f"POST {path} failed: {e}")

if __name__ == '__main__':
    base = 'http://127.0.0.1:8000'
    print('Starting endpoint tests against', base)
    do_get('/')
    do_get('/health')

    do_post('/api/v1/explain/text', {"chapter_text": "Photosynthesis is the process by which plants convert light energy into chemical energy.", "output_language":"english"})

    do_post('/api/v1/illustration', {"prompt":"leaf cell diagram","topic_hint":"Photosynthesis","visual_kind":"diagram","style":"diagramPro"})

    do_post('/api/v1/flashcards/generate', {"topic":"Photosynthesis","card_count":2})

    do_post('/api/v1/quiz/generate', {"topic":"Photosynthesis","question_count":2})

    do_post('/api/v1/slides/generate', {"topic":"Photosynthesis","slide_count":2})

    do_post('/api/v1/infographic/generate', {"topic":"Photosynthesis"})

    do_post('/api/v1/audio/speech', {"context_text":"Photosynthesis converts light energy into chemical energy; plants capture sunlight to make sugars and release oxygen.", "openai_voice":"nova"})

    do_post('/api/v1/video/jobs', {"prompt":"Short explainer: Photosynthesis overview for testing.","stack":"openai","seconds":"4"})

    print('All tests attempted.')
