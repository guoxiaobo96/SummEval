
class Metric:
    def evaluate_example(self, summary, reference):
        raise NotImplementedError

    def evaluate_batch(self, summaries, references, aggregate=True, show_progress_bar=False):
        raise NotImplementedError
