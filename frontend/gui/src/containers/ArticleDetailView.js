import React from 'react';
import axios from 'axios';

import { Card } from 'antd';


class ArticleDetail extends React.Component {

	state = {
		article: {}
	}

	componentDidMount() {
		const articleID = this.props.match.params.articleID;
		console.log({articleID});

		axios.get(`http://localhost:8000/react_sample/${articleID}`)
		.then(res => {
			this.setState({
				articles: res.data
			});
			console.log(res.data);
		})
	}

	render() {
		return (
			<Card title={this.state.article.title}>
				<p>{this.state.article.content}</p>
			</Card>
		)
	}
}

export default ArticleDetail;