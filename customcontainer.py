class container:
    def __init__(this):
        this.tags = {}

    def __getitem__(this, tag):
        return self.tags[tag.lower()] = self.tags.get(tag, 0) + 1
