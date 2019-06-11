import plotly.graph_objs as go


def build_language_graph(df_patients):
    count_english = df_patients.language_cd.str.count('english').sum()
    count_spanish = df_patients.language_cd.str.count('spanish').sum()
    count_german = df_patients.language_cd.str.count('german').sum()
    return {
        'data': [go.Bar(
            x=['Englisch', 'Spanisch', 'Deutsch'],
            y=[count_english, count_spanish, count_german],
            marker=dict(color=['#4da6ff', '#4da6ff', '#4da6ff'],
                        line=dict(color='#a3a3c2', width=2)),
        ),
        ],

        'layout': go.Layout(
            title='Verteilung nach Muttersprache',
        )
    }
