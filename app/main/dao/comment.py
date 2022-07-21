class Comment:
    """Class Comment for DAO"""
    def __init__(self,
                 post_id=0,
                 commenter_name="",
                 comment="",
                 pk=""
                 ):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk
