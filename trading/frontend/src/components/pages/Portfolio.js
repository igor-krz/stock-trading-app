import React, { Component } from 'react';

class Portfolio extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data = {}
        }
    }
    
    onLoad = () => {
        // Get data from api endpoint
    }

    componentDidMount() {
        this.onLoad()
    }

    render() {
        return (
            <div>
                <div>
                    <h3>Value: {}</h3>
                    <h3>balance: {}</h3>
                    <Link to='/graph'><button>Add Stock to Watchlist</button></Link>
                    <button onClick={this.buy()}Buy></button>
                    <button onClick={this.sell()}>Sell</button>
                </div>
            </div>
        );
    }
}

export default Portfolio;