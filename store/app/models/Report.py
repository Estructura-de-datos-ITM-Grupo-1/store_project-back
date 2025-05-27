# Este archivo puede definirse si quieres usar lógica de construcción de reportes como clase

class ReportModel:
    def __init__(self, title: str, summary: dict):
        self.title = title
        self.summary = summary

    def to_dict(self):
        return {
            "title": self.title,
            "summary": self.summary,
        }
