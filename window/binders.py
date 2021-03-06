class BindersMixIn:
    def bind_handlers(self):
        self.bind("<Configure>", self.on_resize)
        self.bind('<Button>', self.force_redraw_image)
        self.bind('<KeyRelease>', self.on_key_release)
        self.bind('<Control-b>', self.exec_btn_handler)
        self.imagepreview.bind('<Control-Button>', self.show_image)
        self.seedinput.bind('<KeyRelease>', self.validate_seed)
        self.seedrandom.bind('<Button>', self.update_seed)
        self.execbutton.bind('<Control-Button>', self.update_and_execute)
        self.execbutton.bind('<Button>', self.exec_btn_handler)
        self.loadcodebutton.bind('<Button>', self.load_code_button_handler)
        self.savecodebutton.bind('<Button>', self.save_code_button_handler)
        self.loadimagebutton.bind('<Button>', self.load_image_button_handler)
        self.saveimagebutton.bind('<Button>', self.save_image_button_handler)
