import numpy as np

from chatty import speech_acts, sentiment
from chatty.extractors import conversation_to_utterances
from chatty.utils import cleaning


def _tag(utterances):
    parsed = dict()
    parsed.update({'utterances': utterances})
    parsed.update(speech_acts.parse(utterances))
    parsed.update(sentiment.parse(utterances))
    next_utterance_pred = sentiment.parse_next(parsed)
    parsed.update(next_utterance_pred)
    return parsed


def analyze_slack(text):
    utterances = conversation_to_utterances(text)
    return _tag(utterances)


def analyze(utterances):
    return _tag(utterances)
