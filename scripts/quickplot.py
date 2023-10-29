import numpy as np
from matplotlib import pyplot as plt


def QuickPlot(data_x, data_y, **kwargs):
    
    # Font Family Set
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False 
    
    ############################################# Parameters Config ################################################
    
    # Assert whether the given two groups data are same in the shape
    if data_x.shape != data_y.shape:
        raise ValueError('You have to ensure the shape of the two data groups!')
        
    # Get the number of the groups of values in each group of data
    num_of_plot = 1 if len(data_x.shape)==1 else data_x.shape[0]
    # Get How many columns per row
    fig_columns = 1 if 'fig_columns' not in kwargs.keys() else kwargs['fig_columns']
    fig_rows = (num_of_plot//fig_columns)+(1 if num_of_plot%fig_columns != 0 else 0)
    
    # Define the figure
    f = plt.figure(dpi=300 if 'dpi' not in kwargs.keys() else kwargs['dpi'],
                   figsize=(fig_columns*3.5, fig_rows*2.5))
    
    # Get the type(s) of plot
    plot_types = ['plot']*num_of_plot if 'plot_types' not in kwargs.keys() else kwargs['plot_types']
        
    # Get the label(s) and title(s) of plot
    labels = [['X', 'Y']]*num_of_plot if 'labels' not in kwargs.keys() else kwargs['labels']
    titles = [f'figure {i}.' for i in range(1, num_of_plot+1)] if 'titles' not in kwargs.keys() else kwargs['titles']
    # Get the colors
    if 'colors' not in kwargs.keys():
        # Get the config of color(s) and marker(s)
        colors = ['deepskyblue']*num_of_plot
        # Set hist default color to 'grey' and  rainbow color list to pie
        for i in range(num_of_plot):
            if plot_types[i] == 'hist':
                colors[i] = 'grey'
            elif plot_types[i] == 'pie':
                colors[i] = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
    else:
        colors = kwargs['colors']
        
    markers = [',']*num_of_plot if 'markers' not in kwargs.keys() else kwargs['markers']
    
    ####### Scatter Config ########
    
    # Get the size of each point while using scatter
    sca_num = plot_types.count('scatter')
    point_s = [[20]]*sca_num if 'point_s' not in kwargs.keys() else kwargs['point_s']
    
    ###### End Scatter Config #####
    
    ####### Bar Config ########
    
    # Get the number of bar
    bar_num = plot_types.count('bar')
    
    # Get the width(series) of each bar
    bar_widths = [[0.6]]*bar_num if 'bar_widths' not in kwargs.keys() else kwargs['bar_widths']
    # Get the interval between each bar
    bar_paddings = [[0]]*bar_num if 'bar_paddings' not in kwargs.keys() else kwargs['bar_paddings']
    # Get the bottom(series) of each bar
    bar_bottoms = [[0]]*bar_num if 'bar_bottoms' not in kwargs.keys() else kwargs['bar_bottoms']
    # Get the approach of align(series) of each bar
    bar_aligns = ['center']*bar_num if 'bar_aligns' not in kwargs.keys() else kwargs['bar_aligns']
    
    # Outlooking Settings
    # Get the color(series) of each bar's edge
    bar_edgecolors = [['black']]*bar_num if 'bar_edgecolors' not in kwargs.keys() else kwargs['bar_edgecolors']
    # Get the width(series) of each bar's edge
    linewidths = [[0]]*bar_num if 'linewidths' not in kwargs.keys() else kwargs['linewidths']
    # Get the labels of each row index of each bar
    tick_labels = None if 'tick_labels' not in kwargs.keys() else kwargs['tick_labels']
    # Get the padding(s) of each bar
    hatchs = None if 'hatchs' not in kwargs.keys() else kwargs['hatchs']
    
    ###### End Bar Config #####
    
    ####### Heat Config ########
    
    # Get the number of the heat maps
    heat_num = plot_types.count('heat')
    # Cmap Color Pattle
    heat_maps = [plt.cm.autumn]*heat_num if 'heat_maps' not in kwargs.keys() else kwargs['heat_maps']
    # Labels
    map_labels = [] if 'map_labels' not in kwargs.keys() else kwargs['map_labels']
    
    ###### End Heat Config #####
    
    ####### Hist Config ########
    
    # Get the number of the hist maps
    hist_num = plot_types.count('hist')
    
    # Get intervals ---- interval = (1-rwidth) inch
    rwidths = [[0.7]]*hist_num if 'rwidths' not in kwargs.keys() else kwargs['rwidths']
    # Get bins ---- the number of the bars
    bins = [10]*hist_num if 'bins' not in kwargs.keys() else kwargs['bins']
    # Get ranges ---- the extent we focused on
    ranges = None if 'ranges' not in kwargs.keys() else kwargs['ranges']
    # Get densitys ---- Whether a normalization is needed
    densitys = [False]*hist_num if 'densitys' not in kwargs.keys() else kwargs['densitys']
    # Get stackeds ---- Whether the muatual part should be displayed
    stackeds = [False]*hist_num if 'stackeds' not in kwargs.keys() else kwargs['stackeds']
    
    # Get the color(series) of each bar's edge
    hist_edgecolors = [(0, 0, 0)]*hist_num if 'hist_edgecolors' not in kwargs.keys() else kwargs['hist_edgecolors']
    # Get the transparency of each bar
    his_alphas = [1.0]*hist_num if 'his_alphas' not in kwargs.keys() else kwargs['his_alphas']
    
    ###### End Hist Config #####
    
    ####### Pie Config ########
    
    # Get the number of the pie maps
    pie_num = plot_types.count('pie')
    
    # Get offsets from the central point
    explodes = None if 'explodes' not in kwargs.keys() else kwargs['explodes']
    # Get the label for each piece
    pie_labels = None if 'pie_labels' not in kwargs.keys() else kwargs['pie_labels']
    # Get ranges ---- the extent we focused on
    frames = [False]*pie_num if 'frames' not in kwargs.keys() else kwargs['frames']
    # Get densitys ---- Whether a normalization is needed
    normalizes = [True]*pie_num if 'normalizes' not in kwargs.keys() else kwargs['normalizes']
    
    # Decoration Arguments
    # Distance of piece text from the center of the pie
    pctdistances = [0.5]*pie_num if 'pctdistances' not in kwargs.keys() else kwargs['pctdistances']
    # Font Size of the decoration Text
    pie_fontsizes = [12]*pie_num if 'pie_fontsizes' not in kwargs.keys() else kwargs['pie_fontsizes']
    # Whether text information is needed
    pie_per_shows = [True]*pie_num if 'pie_per_shows' not in kwargs.keys() else kwargs['pie_per_shows']
    
    ###### End Pie Config #####
    
    ####### Area Config ########
    
    # Get the number of the area maps
    area_num = plot_types.count('area')
    
    # Get the transparency of each bar
    area_alphas = [1.0]*area_num if 'area_alphas' not in kwargs.keys() else kwargs['area_alphas']
    
    ###### End Area Config #####
    
    ############################################# Ending Config ################################################
    
    # Counters
    # Counter for columns
    col_cnt = 1
    # Counter for scatter
    sca_cnt =  0
    # Counter for bar
    bar_cnt =  0
    # Counter for heat map
    heat_cnt =  0
    # Counter for box map
    box_cnt =  0
    # Counter for hist map
    hist_cnt = 0
    # Counter for pie map
    pie_cnt = 0
    # Counter for area map
    area_cnt = 0
    
    # Start Plot!
    for i in range(num_of_plot):
        # Get respective argument
        
        # Get the data for each graph
        X = data_x if num_of_plot==1 else data_x[i]
        Y = data_y if num_of_plot==1 else data_y[i]
        
        # Get plot type
        plot_type = plot_types[i] if i<len(plot_types) else 'plot'
        
        # Get public outlook parameters
        if plot_type!='pie' and plot_type!='hist':
            color = colors[i] if i<len(colors) else 'deepskyblue'
        elif plot_type=='pie':
            color = colors[i] if i<len(colors) else ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
        else:
            color = colors[i] if i<len(colors) else 'grey'
        marker = markers[i] if i<len(markers) else ','
        
        # Get text information for each figure
        title = titles[i] if i<len(titles) else f'figure {i+1}.'
        label = labels[i] if i<len(labels) else ('X', 'Y')
        
        # Get size arguments for each scatter
        if sca_num != 0:
            s = point_s[sca_cnt] if sca_cnt<len(point_s) else 8
        
        # Get arguments for each bar
        if bar_num != 0:
            # Primary Arguments
            bar_width = bar_widths[bar_cnt] if bar_cnt<len(bar_widths) else 0.6
            bar_bottom = bar_bottoms[bar_cnt] if bar_cnt<len(bar_bottoms) else 0
            bar_align = bar_aligns[bar_cnt] if bar_cnt<len(bar_aligns) else 'center'
            bar_padding = bar_paddings[bar_cnt] if bar_cnt<len(bar_paddings) else 0
            # Extended Arguments
            # Get the color(series) of each bar's edge
            bar_edgecolor = bar_edgecolors[bar_cnt] if bar_cnt<len(bar_edgecolors) else 'black'
            # Get the width(series) of each bar's edge
            linewidth = linewidths[bar_cnt] if bar_cnt<len(linewidths) else 0
            # Get the labels of each row index of each bar
            if tick_labels:
                tick_label = tick_labels[bar_cnt] if bar_cnt<len(tick_labels) else None
            else:
                tick_label = None
            # Get the padding(s) of each bar
            if hatchs:
                hatch = hatchs[bar_cnt] if bar_cnt<len(hatchs) else None
            else:
                hatch = None
                
        # Get the arguments for each heat map
        if heat_num != 0:
            heat_map = heat_maps[heat_cnt] if heat_cnt<len(heat_maps) else plt.cm.autumn
            
        # Get the arguments for each hist map
        if hist_num != 0:
            rwidth = rwidths[hist_cnt] if hist_cnt<len(rwidths) else 0.7
            # Get intevals ---- interval = (1-rwidth) inch
            bin_ = bins[hist_cnt] if hist_cnt<len(bins) else 10
            # Get intevals ---- interval = (1-rwidth) inch
            if ranges:
                range_ = ranges[hist_cnt] if hist_cnt<len(ranges) else None
            else:
                range_ = None
            # Get intevals ---- interval = (1-rwidth) inch
            density = densitys[hist_cnt] if hist_cnt<len(densitys) else False
            # Get intevals ---- interval = (1-rwidth) inch
            stacked = stackeds[hist_cnt] if hist_cnt<len(stackeds) else False
            # Get the color(series) of each bar's edge
            hist_edgecolor = hist_edgecolors[hist_cnt] if hist_cnt<len(hist_edgecolors) else (0, 0, 0)
            # Get the transparency of each bar's edge
            his_alpha = his_alphas[hist_cnt] if hist_cnt<len(his_alphas) else 1.0
            
        # Get the arguments for each pie map
        if pie_num != 0:
            # Get offsets from the central point
            if explodes:
                explode = explodes[pie_cnt] if pie_cnt<len(explodes) else None
            else:
                explode = None
            # Get the label for each piece
            if pie_labels:
                pie_label = pie_labels[pie_cnt] if pie_cnt<len(pie_labels) else None
            else:
                pie_label = None
            # Get ranges ---- the extent we focused on
            frame = frames[pie_cnt] if pie_cnt<len(frames) else False
            # Get densitys ---- Whether a normalization is needed
            normalize = normalizes[pie_cnt] if pie_cnt<len(normalizes) else True
            # Get the distance of the pieces
            pctdistance = pctdistances[pie_cnt] if pie_cnt<len(pctdistances) else 0.5
            # Get the font size
            pie_fontsize = pie_fontsizes[pie_cnt] if pie_cnt<len(pie_fontsizes) else 12
            # Whether need a text information display 
            pie_per_show = pie_per_shows[pie_cnt] if pie_cnt<len(pie_per_shows) else True
            
        # Get the arguments for each pie map
        if area_num != 0:
            # Get transparency
            area_alpha = area_alphas[area_cnt] if area_cnt<len(area_alphas) else 1.0
            
        # Set the Sub Plot
        ax = plt.subplot(fig_rows,
                         fig_columns,
                         i+1)
        col_cnt = col_cnt+1 if col_cnt <= fig_columns else 1
        
        # Plot as corresponding function
        if plot_type == 'plot':
            plt.plot(X, Y, color=color, marker=marker)
        # Scatter
        elif plot_type == 'scatter':
            plt.scatter(X, Y, s=s, c=color, marker=marker)
            sca_cnt += 1
        # Bar
        elif plot_type == 'bar':
            plt.bar(X, Y, width=bar_width, bottom=bar_bottom, align=bar_align, color=color,
                    edgecolor=bar_edgecolor,
                    linewidth=linewidth,
                    tick_label=tick_label,
                    hatch=hatch)
            plt.xticks(rotation=45)
            bar_cnt += 1
        # Heat Map
        elif plot_type == 'heat':
            # Get the unit width
            if len(Y.shape)==1:
                Y_unit_len = int(np.sqrt(Y.shape[0]))
                Y = Y.reshape(Y_unit_len, Y_unit_len)
            else:
                Y_unit_len = Y.shape[0]
            
            # Get the tick labels for each axis
            if heat_cnt>=len(map_labels):
                xLabel = [f'x-{k}' for k in range(Y_unit_len)]
                yLabel = [f'y-{k}' for k in range(Y_unit_len)]
            else:
                xLabel, yLabel = map_labels[heat_cnt]
            
            # Set to the plot
            ax.set_yticks(range(len(yLabel)))
            ax.set_yticklabels(yLabel)
            ax.set_xticks(range(len(xLabel)))
            ax.set_xticklabels(xLabel, rotation=45)
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            
            plt.colorbar(plt.imshow(Y, cmap=heat_map))
            heat_cnt += 1
        # Box Map
        elif plot_type == 'box':
            plt.boxplot(Y)
            box_cnt += 1
        # Hist Plot
        elif plot_type == 'hist':
            plt.hist(Y, color=color, rwidth=rwidth, bins=bin_, 
                     range=range_, density=density, stacked=stacked,
                     edgecolor=hist_edgecolor, alpha=his_alpha)
            hist_cnt += 1
        # Pie Plot
        elif plot_type == 'pie':
            plt.pie(Y, colors=color, labels=pie_label,
                    frame=frame, normalize=normalize,
                    explode=explode,
                    autopct='%.2f%%' if pie_per_show else '',
                    textprops={'fontsize':pie_fontsize},
                    pctdistance=pctdistance)
            pie_cnt += 1
        # Area Plot
        elif plot_type == 'area':
            plt.fill_between(X, Y, color=color, alpha=area_alpha)
            area_cnt += 1
        
        else:
            raise ValueError(f"There is no type named '{plot_type}' supported.")
            
        # Futher settings
        # Set Margins
        plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.5,hspace=0.5)
        # Set the labels
        if plot_type != 'pie':
            plt.xlabel(label[0])
            plt.ylabel(label[1])
        plt.title(title)