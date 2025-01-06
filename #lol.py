    def check_portfolio_impact(self,field):

        self.list_plus_one_fields.append(field)
        
        plus_portfoliovalue = 0
        times = 1000  # Number of simulation runs

        for i in range(times):
            self.run()  # Simulate a run
            self.sort_for_best()  # Sort camels for evaluation

            for color, base_value in self.portfolio.items():
                for place, camel in enumerate(self.camle_list):
                    if camel.color == color:
                        if place == 0:
                            plus_portfoliovalue += base_value
                        elif place == 1:
                            plus_portfoliovalue += 1
                        else:
                            plus_portfoliovalue -= 1

        plus_portfoliovalue = 0
        times = 1000  # Number of simulation runs

        for i in range(times):
            self.run()  # Simulate a run
            self.sort_for_best()  # Sort camels for evaluation

            for color, base_value in self.portfolio.items():
                for place, camel in enumerate(self.camle_list):
                    if camel.color == color:
                        if place == 0:
                            minus_portfoliovalue += base_value
                        elif place == 1:
                            plus_portfoliovalue += 1
                        else:
                            plus_portfoliovalue -= 1
        

        # Print or return the final portfolio value
        print(f"Total portfolio impact: {portfolio_value}")
        return portfolio_value  