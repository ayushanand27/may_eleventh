import json
import urllib.request

BASE = 'http://127.0.0.1:8000'
CHAPTER = (
    'Photosynthesis is the process by which plants convert light energy into chemical energy. '
    'It uses chlorophyll to capture sunlight and produces glucose and oxygen.'
)


def get(path: str) -> None:
    with urllib.request.urlopen(BASE + path, timeout=30) as r:
        body = r.read().decode('utf-8', 'replace')
        print(f'GET {path} -> {r.status}')
        print(body[:500])


def post_json(path: str, payload: dict) -> None:
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(BASE + path, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    with urllib.request.urlopen(req, timeout=180) as r:
        body = r.read().decode('utf-8', 'replace')
        print(f'POST {path} -> {r.status}')
        print(body[:1200])


if __name__ == '__main__':
    print('Starting Learn-only endpoint sweep against', BASE)
    get('/health')
    post_json('/api/v1/explain/text', {
        'chapter_text': CHAPTER,
        'output_language': 'english',
        'topic_hint': 'Photosynthesis',
    })
    post_json('/api/v1/quiz/generate', {
        'topic': 'Photosynthesis',
        'context_text': CHAPTER,
        'output_language': 'english',
        'stack': 'openai',
        'question_count': 4,
        'difficulty': 'standard',
    })
    post_json('/api/v1/flashcards/generate', {
        'topic': 'Photosynthesis',
        'context_text': CHAPTER,
        'output_language': 'english',
        'stack': 'openai',
        'card_count': 4,
    })
    post_json('/api/v1/slides/generate', {
        'topic': 'Photosynthesis',
        'context_text': CHAPTER,
        'output_language': 'english',
        'stack': 'openai',
        'slide_count': 4,
    })
    post_json('/api/v1/infographic/generate', {
        'topic': 'Photosynthesis',
        'context_text': CHAPTER,
        'output_language': 'english',
        'stack': 'openai',
    })
    post_json('/api/v1/audio/speech', {
        'context_text': CHAPTER,
        'output_language': 'english',
        'stack': 'openai',
        'openai_voice': 'nova',
        'openai_tts_model': 'tts-1',
    })
    print('Done.')
