import matplotlib.pyplot as plt  # type: ignore

class dataVisualization:

    @staticmethod
    def plotTopObjs(x_data, y_data, x_label: str, y_label: str):
        fig, ax = plt.subplots(figsize=(10, 6)) 
        bars = ax.bar(x_data, y_data, color='skyblue') 

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:,.2f}', va='bottom', ha='center') 

        ax.set_xlabel(x_label, fontsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.set_title(f'Top 5 {x_label} por {y_label}', fontsize=16) 
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45, ha='right') 
        plt.tight_layout() 
        plt.show()
    
    @staticmethod
    def plotLineObjs(x_data, y_data, x_label: str, y_label: str):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_data, y_data, marker='o', linestyle='-', color='coral') 

        for i, txt in enumerate(y_data):
            ax.annotate(f'{txt:,.2f}', (x_data[i], y_data[i]), textcoords="offset points", xytext=(0,10), ha='center')

        ax.set_xlabel(x_label, fontsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.set_title(f'{y_label} por {x_label}', fontsize=16)
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()