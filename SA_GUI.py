
import wx
import wx.xrc
import wx.grid


class SAFrame(wx.Frame):
    # derive from frame a new class
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='SA thingy', pos=wx.DefaultPosition,
                          size=wx.Size(840, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        '''' set up Menu'''
        self.m_menubar = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        self.open_file = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Open", u"Open an existing TSP file", wx.ITEM_NORMAL)
        self.file_menu.Append(self.open_file)

        self.save_file = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Save", u"Save a TSP into a file", wx.ITEM_NORMAL)
        self.file_menu.Append(self.save_file)

        self.file_menu.AppendSeparator()

        self.exit = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Exit", u"Terminate the program", wx.ITEM_NORMAL)
        self.file_menu.Append(self.exit)

        self.m_menubar.Append(self.file_menu, u"File")

        self.about_menu = wx.Menu()
        self.info = wx.MenuItem(self.about_menu, wx.ID_ANY, u"Info", u"Provides info on the program", wx.ITEM_NORMAL)
        self.about_menu.Append(self.info)

        self.m_menubar.Append(self.about_menu, u"About")

        self.SetMenuBar(self.m_menubar)

        '''creates a status bar in the bottom of the window'''
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        ''' set up sizer for GUI layout '''
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Parameters"), wx.VERTICAL)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.max_tmp = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize,
                                   0)
        gSizer3.Add(self.max_tmp, 0, wx.ALL, 5)

        self.maxTemp = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Max Temperature", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.maxTemp.Wrap(-1)
        gSizer3.Add(self.maxTemp, 0, wx.ALL, 5)

        self.min_tmp = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        gSizer3.Add(self.min_tmp, 0, wx.ALL, 5)

        self.MinTemp = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Min Temperature", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.MinTemp.Wrap(-1)
        gSizer3.Add(self.MinTemp, 0, wx.ALL, 5)

        self.m_alph = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        gSizer3.Add(self.m_alph, 0, wx.ALL, 5)

        self.alpha = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Alpha", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alpha.Wrap(-1)
        gSizer3.Add(self.alpha, 0, wx.ALL, 5)

        self.iter_num = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        gSizer3.Add(self.iter_num, 0, wx.ALL, 5)

        self.iterations = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Iteration Number", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.iterations.Wrap(-1)
        gSizer3.Add(self.iterations, 0, wx.ALL, 5)

        sbSizer5.Add(gSizer3, 1, wx.EXPAND, 5)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(sbSizer5.GetStaticBox(), wx.ID_ANY, u"label"), wx.VERTICAL)

        self.m_toggleBtn1 = wx.ToggleButton(sbSizer11.GetStaticBox(), wx.ID_ANY, u"Solve!", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        sbSizer11.Add(self.m_toggleBtn1, 0, wx.ALL, 5)

        self.init_sol = wx.Panel(sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                 wx.TAB_TRAVERSAL)
        self.init_sol.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        sbSizer11.Add(self.init_sol, 1, wx.EXPAND | wx.ALL, 5)

        sbSizer5.Add(sbSizer11, 1, wx.EXPAND, 5)

        fgSizer1.Add(sbSizer5, 1, wx.EXPAND, 5)

        sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Data"), wx.HORIZONTAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.init_graph = wx.Panel(sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 50),
                                   wx.TAB_TRAVERSAL)
        self.init_graph.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer4.Add(self.init_graph, 1, wx.EXPAND | wx.ALL, 5)

        self.tspdata = wx.grid.Grid(sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        ''' set up the Grid for TSP data '''
        self.tspdata.CreateGrid(10, 2)
        self.tspdata.EnableEditing(True)
        self.tspdata.EnableGridLines(True)
        self.tspdata.SetGridLineColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.tspdata.EnableDragGridSize(False)
        self.tspdata.SetMargins(0, 0)

        # Columns
        self.tspdata.EnableDragColMove(False)
        self.tspdata.EnableDragColSize(True)
        self.tspdata.SetColLabelSize(30)
        self.tspdata.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.tspdata.EnableDragRowSize(True)
        self.tspdata.SetRowLabelSize(80)
        self.tspdata.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.tspdata.SetLabelBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        # Cell Defaults
        self.tspdata.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        fgSizer4.Add(self.tspdata, 0, wx.ALIGN_TOP | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        ''' sizers configure '''
        self.m_panel22 = wx.Panel(sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        fgSizer4.Add(self.m_panel22, 1, wx.EXPAND | wx.ALL, 5)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        self.m_toggleBtn6 = wx.ToggleButton(sbSizer9.GetStaticBox(), wx.ID_ANY, u"import data", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gSizer7.Add(self.m_toggleBtn6, 0, wx.ALL, 5)

        self.m_toggleBtn7 = wx.ToggleButton(sbSizer9.GetStaticBox(), wx.ID_ANY, u"export data", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gSizer7.Add(self.m_toggleBtn7, 0, wx.ALL, 5)

        fgSizer4.Add(gSizer7, 1, wx.EXPAND, 5)

        sbSizer9.Add(fgSizer4, 1, wx.EXPAND, 5)

        fgSizer1.Add(sbSizer9, 1, wx.EXPAND, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Optimization"), wx.VERTICAL)

        self.optimize = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"Optimize!", wx.DefaultPosition, wx.DefaultSize,
                                  0)
        sbSizer6.Add(self.optimize, 0, wx.ALL, 5)

        self.opt_sol = wx.Panel(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(50, 50),
                                wx.TAB_TRAVERSAL)
        self.opt_sol.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        sbSizer6.Add(self.opt_sol, 1, wx.EXPAND | wx.ALL, 5)

        self.opt_par = wx.Panel(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                wx.TAB_TRAVERSAL)
        self.opt_par.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        sbSizer6.Add(self.opt_par, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(sbSizer6, 1, wx.EXPAND, 5)

        sbSizer10 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Opt. graph"), wx.VERTICAL)

        self.opt_graph = wx.Panel(sbSizer10.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 200),
                                  wx.TAB_TRAVERSAL)
        self.opt_graph.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        sbSizer10.Add(self.opt_graph, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(sbSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        ''' Connect events '''
        self.Bind(wx.EVT_MENU, self.on_open, id=self.open_file.GetId())
        self.Bind(wx.EVT_MENU, self.on_save, id=self.save_file.GetId())
        self.Bind(wx.EVT_MENU, self.on_exit, id=self.exit.GetId())
        self.Bind(wx.EVT_MENU, self.on_About, id=self.info.GetId())
        self.max_tmp.Bind(wx.EVT_TEXT, self.on_maxtemp)
        self.min_tmp.Bind(wx.EVT_TEXT, self.on_mintemp)
        self.m_alph.Bind(wx.EVT_TEXT, self.on_alpha)
        self.iter_num.Bind(wx.EVT_TEXT, self.on_iteration)
        self.m_toggleBtn1.Bind(wx.EVT_TOGGLEBUTTON, self.on_solve)
        self.m_toggleBtn6.Bind(wx.EVT_TOGGLEBUTTON, self.on_import)
        self.m_toggleBtn7.Bind(wx.EVT_TOGGLEBUTTON, self.on_export)
        self.optimize.Bind(wx.EVT_BUTTON, self.on_optimize)

        self.Show()
    def __del__(self):
        pass

    ''' define Events '''

    def on_open(self, event):
        event.Skip()

    def on_save(self, event):
        event.Skip()

    def on_exit(self, event):
        self.Close(True)

    def on_About(self, event):
        # show a dialog with OK button
        dlg = wx.MessageDialog(self, "This programs enables the user to input a TSP as a problem on XY axis, "
                                     "and using Simulated Annealing algorithm parameters that the user enters the "
                                     "program solves the TSP and gives and initial good solution. Later the user can "
                                     "choose to optimize the parameters for the algorithm which should introduce better"
                                     " results.", "About the program and SA", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


    def on_maxtemp(self, event):
        event.Skip()

    def on_mintemp(self, event):
        event.Skip()

    def on_alpha(self, event):
        event.Skip()

    def on_iteration(self, event):
        event.Skip()

    def on_solve(self, event):
        event.Skip()

    def on_import(self, event):
        event.Skip()

    def on_export(self, event):
        event.Skip()

    def on_optimize(self, event):
        event.Skip()


app = wx.App(False)  # does not redirects stdout to a window
frame = SAFrame(None)  # frame is the top level window
app.MainLoop()