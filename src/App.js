import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      message: null,
    }
  }

  componentDidMount() {
    fetch('/api/message')
      .then(res => res.json())
      .then(data => this.setState({ message: data.message }));

  }

  render() {
    const message = this.state.message;

    return (
      <div>
        Message From API: {message}
      </div>
    )
  }
}

export default App;
