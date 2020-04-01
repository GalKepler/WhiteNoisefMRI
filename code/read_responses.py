import pandas as pd
import pathlib, os
from pathlib import Path
import matplotlib.pyplot as plt
from stimuli import Stimuli, responses
import numpy as np

CSV_PATH = pathlib.Path(
    "/Users/dumbeldore/Desktop/White_Noise_fMRI/labeling_exp/Stimuli labeling for fMRI task.csv"
)
STIMULI = Stimuli
RESPONSES = responses


class ResponseCsv:
    def __init__(
        self, figures_dir: os.PathLike = None, csv_path: os.PathLike = CSV_PATH
    ):
        """
        A class that manipluates and calculates data from the responses csv.
        Arguments:
            csv_path {os.PathLike} -- [Path to csv]
        """
        if not figures_dir:
            self.figures_dir = Path(csv_path).parent / "responses"
        else:
            figures_dir = Path(figures_dir)
            self.figures_dir = figures_dir
        if not Path(self.figures_dir).is_dir():
            self.figures_dir.mkdir()
            print(f"Generated directory for reponses figures in {self.figures_dir}")
        self.df = pd.read_csv(csv_path).drop("Timestamp", axis=1)
        self.stim_dict = self.gen_dict()
        self.transform_answers(self.stim_dict)

    def gen_dict(self):
        """
        Generates stimuli's dictionary, where keys are stimuli and values are paths and dataframes
        Returns:
            [type] -- [description]
        """
        stimuli_dict = dict()
        for i, stim in enumerate(STIMULI):
            stimuli_dict[stim.name] = dict(stimulus_path=stim.value)
            rel_df = self.df.iloc[:, i * 2 : i * 2 + 2]
            stimuli_dict[stim.name]["responses"] = rel_df
        return stimuli_dict

    def transform_answers(self, stim_dict: dict):
        """
        Transform subject's answer to numeric values
        Arguments:
            stim_dict {dict} -- [dictionary containing stimuli's data]
        """
        new_ind = [resp.name for resp in RESPONSES]
        for stim in stim_dict:
            df = stim_dict[stim]["responses"]
            df = df.fillna("empty")
            new_df = pd.DataFrame(columns=df.columns, index=new_ind)
            for col in new_df.columns:
                for row in new_df.index:
                    new_df[col][row] = 0
                    for subj in df.index:
                        if row in df[col][subj]:
                            new_df[col][row] += 1
            new_df.columns = ["Feelings", "Familiarity"]
            stim_dict[stim]["transformed_responses"] = new_df
        self.stim_dict = stim_dict

    def generate_figures(self):
        for stim in self.stim_dict:
            df = self.stim_dict[stim]["transformed_responses"]
            header = f"{stim}-{self.stim_dict[stim]['stimulus_path'].name}"
            fig = self.generate_stim_figure(df)
            fig.suptitle(header, fontsize=16)
            fig.savefig(self.figures_dir / f"{header}.png")
            plt.close()

    def generate_stim_figure(self, df: pd.DataFrame):
        """
        Generate pie charts to describe stimulus` data
        Arguments:
            df {pd.DataFrame} -- [stimulus DataFrame]
        """
        fig, axs = plt.subplots(1, 2, figsize=(10, 5), subplot_kw=dict(aspect="equal"))
        for i, col in enumerate(df.columns):
            non_emptys = df[col] > 0
            labels = df.index[non_emptys]
            sizes = df[col].values[non_emptys]
            wedges, texts, autotexts = axs[i].pie(
                sizes,
                labels=labels,
                autopct=lambda pct: func(pct, sizes),
                shadow=True,
                startangle=90,
                textprops=dict(color="w"),
            )
            axs[i].set(title=col)
            axs[i].legend(
                wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1)
            )
            plt.tight_layout()
            plt.setp(autotexts, size=8, weight="bold")
        return fig


def func(pct, allvals):
    absolute = int(pct / 100.0 * np.sum(allvals))
    return "{:.1f}%\n({:d} resp.)".format(pct, absolute)


if __name__ == "__main__":
    resp = ResponseCsv()
    resp.generate_figures()
