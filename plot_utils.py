import io
import matplotlib.pyplot as plt
import seaborn as sns

def try_execute_code(code, df):
    buf = io.BytesIO()
    plt.close("all")
    locs = {"df": df, "plt": plt, "sns": sns}
    try:
        exec(code, {}, locs)
        fig = plt.gcf()
        fig.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)
        plt.close(fig)
        return buf, None
    except Exception as e:
        return None, str(e)