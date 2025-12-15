import wx
from logic import CODE_LENGTH, COLORS, generate_code, on_submit

# -----------------------------
# UI Class
# -----------------------------

class MastermindFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mastermind (wxPython)", size=(480, 650))

        panel = wx.Panel(self)
        main_vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Mastermind")
        title.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 10)

        # Available colors
        color_box = wx.StaticBox(panel, label="Available Colors")
        color_sizer = wx.StaticBoxSizer(color_box, wx.HORIZONTAL)
        color_map = {"R": "RED", "G": "GREEN", "B": "BLUE", "Y": "YELLOW"}

        for c in COLORS:
            p = wx.Panel(panel, size=(40, 40))
            p.SetBackgroundColour(color_map[c])
            color_sizer.Add(p, 0, wx.ALL, 5)
        main_vbox.Add(color_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Explanation
        explain = wx.StaticText(
            panel,
            label="White = Correct color & correct position\nBlack = Correct color but wrong position"
        )
        explain.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_vbox.Add(explain, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # Radio boxes for guesses
        radio_box = wx.StaticBox(panel, label="Select Your Guess (Position 1–4)")
        radio_sizer = wx.StaticBoxSizer(radio_box, wx.HORIZONTAL)

        self.radio_choices = []
        for i in range(CODE_LENGTH):
            rb = wx.RadioBox(
                panel,
                label=f"P{i+1}",
                choices=COLORS,
                majorDimension=4,
                style=wx.RA_SPECIFY_ROWS
            )
            self.radio_choices.append(rb)
            radio_sizer.Add(rb, 0, wx.ALL, 10)
        main_vbox.Add(radio_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Submit button
        submit_btn = wx.Button(panel, label="Submit Guess")
        submit_btn.Bind(wx.EVT_BUTTON, lambda event: on_submit(self))
        main_vbox.Add(submit_btn, 0, wx.ALIGN_CENTER | wx.TOP, 10)

        # History box
        history_box = wx.StaticBox(panel, label="Attempts / Feedback")
        history_sizer = wx.StaticBoxSizer(history_box, wx.VERTICAL)
        self.history = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
        history_sizer.Add(self.history, 1, wx.EXPAND | wx.ALL, 5)
        main_vbox.Add(history_sizer, 1, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(main_vbox)

        # Initialize code and attempt
        self.code = generate_code()
        self.attempt = 1

        self.Show()


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    app = wx.App()
    MastermindFrame()
    app.MainLoop()
