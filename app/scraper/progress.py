
class Progress:
    def __init__(self, current, total) -> None:
        self.current = current
        self.total = total
        pass

    def print_progress(self, current) -> None:
        self.current = current
        progress = current / self.total
        bar_length = 40
        progress_bar = (
            "["
            + "=" * int(bar_length * progress)
            + "-" * (bar_length - int(bar_length * progress))
            + "]"
        )
        print(
            "\rProgress: [{:<40}] {:.2%} {} of {}".format(
                progress_bar, progress, current, self.total
            )
        )
        
        
    # def print_progress(self, current) -> None:
    #     # Update the current value
    #     self.current = current
    #     label = st.empty()
    #     # Calculate the progress
    #     progress = current / self.total
    #     # Display the progress
    #     label.text(f"Progress: {progress:.2%} {current} of {self.total}")
    #     st.progress(progress)
