import React from 'react';

class Reporter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      report: null
    };
  }

  componentDidMount() {
    const { reportName } = this.props.match.params;
    fetch(`/api/reports/${reportName}${this.props.location.search}`)
      .then(res => res.text())
      .then(report => this.setState({ report }))
      .catch(e => console.error(e));
  }

  render() {
    const report = this.state.report;
    // Can't even be asked to do something clever, just going to dangerously set html
    return (
      <div>
        { report ? (<div dangerouslySetInnerHTML={{__html: report}} />) : (<h1>Getting you that report</h1>) }
      </div>
    )
  }
}

export default Reporter;
